from github import Github
import datetime



# todays_date = str(datetime.date.today())
# current_time = datetime.datetime.now().strftime('%Hh%Mm')


# time_with_date = current_time.strftime("%d%B_%Hh%Mm")
# access_token = "qfqegbwdsfvd"
# g = Github("access_token")
g = Github("<userName>", "<Password>")

repo = g.get_repo("PyGithub/PyGithub")


def new_branch_from_base(get_repo_name, get_base_branch, commit_id):
    target_branch = get_base_branch+"_"+ str(datetime.date.today()) +"_"+ datetime.datetime.now().strftime('%Hh%Mm')
    print("New Branch created:"+ target_branch)
    repo = g.get_user().get_repo(get_repo_name)
    newly_created_branch = repo.create_git_ref(ref='refs/heads/' + target_branch, sha=commit_id)
    return str(newly_created_branch)
