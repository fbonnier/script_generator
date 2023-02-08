import os
import sys
import argparse
import json as json
import warnings
# from check_model import instance_kgv2 as instance2
# from check_model import instance_kgv3 as instance3
# from check_model import instance as instance

def get_runscript_from_workflow (workdir, workflow_run, workflow_data):
    runscript_file = None
    if (workflow_run):
        pass
    return runscript_file 

def get_runscript_from_code (workdir, environment, pre_instruction, code, inputs, outputs, instruction):
    runscript_file = None

    return runscript_file

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate HBP model instance runscript from metadata JSON file")

    parser.add_argument("--json", type=argparse.FileType('r'), metavar="JSON Metadata file", nargs=1, dest="json", default="",\
    help="JSON File that contains Metadata of the HBP model to run")

    # parser.add_argument("--kg", type=int, metavar="KG Version", nargs=1, dest="kg", default=int(os.environ.get("KG_VERSION", 2)),\
    # help="Version number of Knowledge Graph to use")

    args = parser.parse_args()


    # Load JSON data
    json_file = args.json[0]
    if not json_file:
        print ("Fatal Error:  Invalid JSON File, please give a valid JSON file using \"--json <path-to-file>\"")
        exit(1)
    json_data = json.load(json_file)

    # Load workdir
    workdir = json_data["Metadata"]["workdir"]

    # Load workflow
    workflow_run_file = json_data["Metadata"]["workflow"]["run"]
    workflow_data_file = json_data["Metadata"]["workflow"]["data"]

    # Load inputs
    inputs = json_data["Metadata"]["run"]["inputs"]

    # Load outputs
    outputs = json_data["Metadata"]["run"]["outputs"]

    # Load environment
    environment = json_data["Metadata"]["run"]["environment"]

    # Load pre-instruction
    pre_instruction = json_data["Metadata"]["run"]["pre-instruction"]

    # Load code
    code = { "url": json_data["Metadata"]["run"]["url"], "path": json_data["Metadata"]["run"]["path"]}

    # Load instruction
    instruction = json_data["Metadata"]["run"]["instruction"]

    runscript_file = None

    # Write runscript file from workflow
    runscript_file = get_runscript_from_workflow (workdir, environment, workflow_run_file, workflow_data_file)

    # Write runscript file from runscript
    if (not runscript_file):
        runscript_file = get_runscript_from_code (workdir, environment, pre_instruction, code, inputs, outputs, instruction)

    # model_instance = None
    ## Create Instance object
    # model_instance = instance3.KGV3_Instance(model_id, token=auth_token)
    # model_instance = instance.Instance(json_file.name)


    # model_instance.create_script_file(work_dir)
    # model_instance.write_code_location()
    # model_instance.write_code_unzip ()
    # model_instance.write_goto_project_folder()
    # model_instance.write_download_inputs()
    # model_instance.write_pip_installs()
    # # model_instance.write_download_results()

    # model_instance.write_watchdog()
    # model_instance.write_code_run()
    # model_instance.write_watchdog_kill()
    # model_instance.close_script_file()
    # print (model_instance.metadata)
    # Exit Done ?
    print ("Done.\n ----- Exit SUCCESS")
