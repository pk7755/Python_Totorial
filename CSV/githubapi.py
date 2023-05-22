import csv
import requests
import pandas as pd


url = 'https://api.github.com/search/repositories?q=stars:%3E1&sort=stars'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response_API = requests.request("GET",url,headers=headers,data={})
status = response_API.status_code
myjson = response_API.json()
# print(myjson)

ourdata = []
csvheaders = ['id','node_id','name','full_name','private''owner','html_url','description',"fork",'url','forks_url','keys_url','collaborators_url','teams_url','hooks_url','issue_events_url','events_url','assignees_url','branches_url','tags_url','blobs_url','git_tags_url','git_refs_url','trees_url','statuses_url','languages_url','stargazers_url','contributors_url','subscribers_url','subscription_url','commits_url','git_commits_url','comments_url','issue_comment_url','contents_url','compare_url','merges_url','archive_url','downloads_url','issues_url','pulls_url','milestones_url','notifications_url',"labels_url",'releases_url','deployments_url','created_at','updated_at','pushed_at','git_url','ssh_url','clone_url','svn_url','homepage','size','stargazers_count','watchers_count','language','has_issues','has_projects','has_downloads','has_wiki','has_pages','has_discussions','forks_count','mirror_url','archived','disabled','open_issues_count','license','allow_forking','is_template','web_commit_signoff_required','topics','visibility','forks','open_issues','watchers','default_branch','score']

for i in myjson['items']:
    listing = [i['id'],i['node_id'],i['name'],i['full_name'],i['private'],i['owner'],i['html_url'],i['description'],i["fork"],i['url'],i['forks_url'],i['keys_url'],i['collaborators_url'],i['teams_url'],i['hooks_url'],i['issue_events_url'],i['events_url'],i['assignees_url'],i['branches_url'],i['tags_url'],i['blobs_url'],i['git_tags_url'],i['git_refs_url'],i['trees_url'],i['statuses_url'],i['languages_url'],['stargazers_url'],i['contributors_url'],i['subscribers_url'],i['subscription_url'],i['commits_url'],['git_commits_url'],i['comments_url'],i['issue_comment_url'],i['contents_url'],i['compare_url'],i['merges_url'],i['archive_url'],i['downloads_url'],i['issues_url'],i['pulls_url'],i['milestones_url'],i['notifications_url'],i["labels_url"],i['releases_url'],i['deployments_url'],i['created_at'],i['updated_at'],i['pushed_at'],i['git_url'],i['ssh_url'],i['clone_url'],['svn_url'],i['homepage'],i['size'],i['stargazers_count'],i['watchers_count'],i['language'],i['has_issues'],['has_projects'],i['has_downloads'],i['has_wiki'],i['has_pages'],i['has_discussions'],i['forks_count'],i['mirror_url'],i['archived'],i['disabled'],i['open_issues_count'],i['license'],['allow_forking'],i['is_template'],i['web_commit_signoff_required'],i['topics'],i['visibility'],i['forks'],i['open_issues'],i['watchers'],i['default_branch'],i['score']]
    ourdata.append(listing)
# print(ourdata)

with open("GitHubApi.csv", "w" ,encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(csvheaders)
    writer.writerows(ourdata)

df = pd.read_csv(r'GitHubApi.csv')


