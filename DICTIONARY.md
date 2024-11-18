# Data Dictionary for the Files in data.zip 
The files in this collection are centered on activity that occurs around some of the most critical open source software projects currently in use. Specifically, these are projects in the "Cloud Native Computing Foundation", or "CNCF". You can learn more about the CNCF at https://cncf.io. CNCF projects are organized into three lifecycle categories: 
1. Sandbox - Projects that are currently being explored. These are new projects that may or may not emerge to become parts of core infrastructure. They are exploratory, and are generally targeted at laying the foundations for new and emerging core infrastructure. 
2. Incubating - Projects that have moved past the exploratory (sandbox) stage, where a determination was made by the CNCF's technical steering committee (TSC) that there is significant promise, and investment should be made to advance these projects into wider use. Such determinations arise from a combination of successful sandbox development and the emergence of a clear and specific purpose and role for each project in future core infrastructure. 
3. Graduated - These are the projects that are currently recognized as "core instrastructure" by the technology firms who are members of the CNCF (which, candidly, is nearly all technology firms). The most prominent example of a project like this Kubernetes, which began as a project within Google to provide a technical foundation for an open source version of Amazon's EC2 infrastructure. The path Kubernetes followed from an internal Google project to one shared and contributed to within the CNCF is one of potential paths that can be followed from conception (sandbox) to utility (graduated). This is one of Google's usual path for contributing to open source infrastrcuture. 

## Network Data
### network_sandbox_orgs.csv
Columns:
  1. cntrb_id
  2. repo_id
  3. action
  4. action_year
  5. action_quarter
  6. counter

### network_incubating_orgs.csv
Columns:
  1. cntrb_id
  2. repo_id
  3. action
  4. action_year
  5. action_quarter
  6. counter

### network_graduated_orgs.csv
Columns:
  1. cntrb_id
  2. repo_id
  3. action
  4. action_year
  5. action_quarter
  6. counter

## Metadata
### repo_info.csv
Columns:
  1. repo_id
  2. repo_group_id
  3. repo_git
  4. repo_path
  5. repo_name
  6. repo_added
  7. repo_type
  8. url
  9. owner_id
  10. description
  11. primary_language
  12. created_at
  13. forked_from
  14. updated_at
  15. repo_archived_date_collected
  16. repo_archived
  17. tool_source
  18. tool_version
  19. data_source
  20. data_collection_date

## cncf_repos_orgs.csv
Columns:
  1. repo_id
  2. category

## action_types.csv
Columns:
  1. action

