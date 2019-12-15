from biz.newBranch import new_branch_from_base
import logging
from flask import jsonify

def validate_repo_info(data):
    get_action_status = data['action']
    get_base_branch = data['pull_request']['base']['ref']
    commit_id = data['pull_request']['base']['sha']
    get_repo_name = data['repository']['name']
    if (( get_action_status == "opened" and get_base_branch == "master" ) or ( get_action_status == "opened" and get_base_branch == "production" )):
        new_branch = new_branch_from_base(get_repo_name, get_base_branch, commit_id)
        return new_branch
    else:
        return jsonify( 
            {
                "Success": "false",
                "Message" : "invalid data"
            }
        )