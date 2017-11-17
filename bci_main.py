import gui.utility.gui_fx
from helpers.save import init_save_data_structure
from helpers.display import init_display_window
from helpers.acquisition_related import init_eeg_acquisition
from bci_tasks.start_task import start_task


def bci_main(parameters, user, exp_type, mode):
    """
    BCI Main.

    Using parameters (dict), user information, exp_type
        ( ex. calibration v. free spell), and mode ( ex .RSVP v. SSVEP)
        the BCI app will initialize a save folder, construct needed information
        and execute the task. This is the main connection between any UI and
        running the app.
    """

    # Define the parameter and data save location
    parameter_location = parameters['parameter_location']['value']
    data_save_location = parameters['data_save_loc']['value']

    # Initalize Save Folder
    save_folder = init_save_data_structure(
        data_save_location, user, parameter_location)

    # Register Task Type
    task_type = {
        'mode': mode,
        'exp_type': exp_type
    }

    # Try executing the task
    try:
        execute_task(
            task_type, parameters, save_folder)

    # Something went wrong, raise exception to caller
    except Exception as e:
        raise e


def execute_task(task_type, parameters, save_folder):
    """
    Excecute Task.

    Executes the desired task by setting up the display window and
        data acquistion, then passing on to the start_task funtion
        which will initialize experiment.
    """

    # Initialize the needed DAQ Parameters
    daq_parameters = {
        'buffer_name': save_folder + '/' + parameters['buffer_name']['value'],
        'device': parameters['acq_device']['value'],
        'filename': save_folder + '/' + parameters['raw_data_name']['value'],
    }

    fake_data = parameters['fake_data']['value']

    if fake_data == 'true':
        server = True
    else:
        server = False

    # Initialize EEG Acquisition
    daq, server = init_eeg_acquisition(daq_parameters, server=server)

    # Initialize Display Window
    display = init_display_window(parameters)

    # Start Task
    try:
        trial_data = start_task(
            daq, display, task_type, parameters, save_folder)
    except Exception as e:
        raise e

    # Stop Acquistion
    daq.stop_acquisition()

    # If a server was started for the data, stop it now.
    if server:
        server.stop()

    # Close the display window
    display.close()

    return trial_data
