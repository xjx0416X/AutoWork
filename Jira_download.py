from jira import JIRA
import os
import pandas as pd
from pandas import DataFrame



jira_server = 'https://taeeint.atlassian.net/'
user_name = 'extern.jianxin.xu@audi.com.cn'
password = 'qazWSX12345678'


jira=JIRA(jira_server,basic_auth=(user_name, password))
Issue_JQL='project = "TPKB" and reporter in (5f719abc459d42006942e506,712020:da9cffff-9567-4c4c-9249-4c76bd2c05a1)and type IN(Bug,Story) and createdDate>=2024-5-1 order by createdDate ASC'

fields = ['key','summary','status', 'created', 'updated','resolved', 'assignee','reporter','sprint']

issues=jira.search_issues(Issue_JQL, maxResults=-1)



class Jira_Handler:

    # 初始化
    def __init__(self, jira_server, user_name, password):
        try:
            self.jira_server = jira_server
            self.user_name = user_name
            self.password = password
            self.jira = JIRA(self.jira_server, basic_auth=(self.user_name, self.password))
        except Exception as e:
            print(e)
        

    def transfrom_to_df(self, issues, fields):
        issues=self.jira.search_issues(Issue_JQL, maxResults=-1)
        try:
            df_issues = DataFrame(columns=fields)
            for issue in issues:
                issue_dict = {}
                for field in fields:
                    if field == 'key':
                        issue_dict[field] = issue.key       

                    elif field =='summary':
                        issue_dict[field] = issue.fields.summary

                    elif field =='status':
                        issue_dict[field] = issue.fields.status.name

                    elif field == 'created':
                        issue_dict[field] = issue.fields.created

                    elif field == 'updated':
                        issue_dict[field] = issue.fields.updated

                    elif field =='resolved':
                        issue_dict[field] = issue.fields.resolutiondate

                    elif field == 'assignee':                        
                        if issue.fields.assignee:
                            issue_dict[field] = issue.fields.assignee.displayName
                        else:
                            issue_dict[field] = None                        

                    elif field =='reporter':                        
                        if issue.fields.reporter:                            
                            issue_dict[field] = issue.fields.reporter.displayName                        
                        else:                            
                            issue_dict[field] = None


                    elif field =='sprint':                        
                        if issue.fields.customfield_10002:                                                        
                            issue_dict[field] = issue.fields.customfield_10002[0]                                                        
                        else:                                                                                                                                
                            issue_dict[field] = None                        


                df_issues = df_issues.append(issue_dict, ignore_index=True)                
            return df_issues
        
        except Exception as e:
            print(e)


