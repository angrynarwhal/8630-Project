# Data Dictionary for the Files in data.zip 
The files in this collection are centered on activity that occurs around some of the most critical open source software projects currently in use. Specifically, these are projects in the "Cloud Native Computing Foundation", or "CNCF". You can learn more about the CNCF at https://cncf.io. CNCF projects are organized into three lifecycle categories: 
1. Sandbox - Projects that are currently being explored. These are new projects that may or may not emerge to become parts of core infrastructure. They are exploratory, and are generally targeted at laying the foundations for new and emerging core infrastructure. 
2. Incubating - Projects that have moved past the exploratory (sandbox) stage, where a determination was made by the CNCF's technical steering committee (TSC) that there is significant promise, and investment should be made to advance these projects into wider use. Such determinations arise from a combination of successful sandbox development and the emergence of a clear and specific purpose and role for each project in future core infrastructure. 
3. Graduated - These are the projects that are currently recognized as "core instrastructure" by the technology firms who are members of the CNCF (which, candidly, is nearly all technology firms). The most prominent example of a project like this Kubernetes, which began as a project within Google to provide a technical foundation for an open source version of Amazon's EC2 infrastructure. The path Kubernetes followed from an internal Google project to one shared and contributed to within the CNCF is one of potential paths that can be followed from conception (sandbox) to utility (graduated). This is one of Google's usual path for contributing to open source infrastrcuture. 
4. Archived (No Data Included) - Archived projects are those that at one time had utility for core infrastructure, and due to the emergence of new technologies that improve or replace them, are no longer actively maintained. In a sense these are a historical record of the CNCF's past. The data is not included because the questions I have, and the questions most people have about open source software projects, center on the present and potential future sustainability and utility. Technological historians may be interested in understanding these projects, but for the purposes of this activity, we are not. 

Data is provided in `.csv` and `.json` formats. The data are identical. Only the physical structure is different. Accordiningly, I explain the `.csv` files below, but the contents of each physical structure are identical. 

## Network Data
Following from the three active categories noted above, each of the next three files contain structured, temporal network data for projects in each of the three CNCF categories. I have broken them down according to these categories because this allows us a more granular understanding of how projects at each phase are functioning. 

The structure of each of these files is identical (and this fact is repeated here, yes). In the next sections I explain the values contained in each field for sandbox because this avoids further repetition. 

### network_sandbox_orgs.csv
Each CNCF project has a single, primary repository. In most cases these primary repositories are one of many specific repositories within a GitHub organization intended to support that open source project. In the interests of maintaining coherence within those primary repositories, functions or features that relate to special use cases, platform specific deployments, and integrations across CNCF projects are usually contained within OTHER, DIFFERENT repositories that are part of the same organization. The resulting cohesiveness of the primary and secondary repositories are a software architecture property. There is a fluid overlap between primary and secondary repository contributors, so the interactions for all of the related respositories are included here. 
#### Columns:
  1. cntrb_id - A algorithmically generated identifier for each contributor to a project. A contributor is a person. 
  2. repo_id - The integer identifier for a specific CNCF respository. (See Metadata section for `repo_info.csv` to get more information about the repositories)
  3. action - These are the 13 specific actions a contributor might perform against a repository. Each of these possible actions is also included in the metadata file `action_types.csv` so that we have a useful, controlled list and can discuss and filter each action type based on our specific questions. For example, some actions are directly related to software contributions. Other actions are related to contributions centered on understanding and explaining needed new features or bug lists, for example. 
  4. action_year - The year the action took place by the contributor, in the repository. 
  5. action_quarter - The quarter the action took place by the contributor in the repository. 
  6. counter - The count, or total number of specific action types taken by a contributor in a repository during the time frame reflected in the action_year+action_month. 

### network_incubating_orgs.csv
#### Columns:
  1. cntrb_id
  2. repo_id
  3. action
  4. action_year
  5. action_quarter
  6. counter

### network_graduated_orgs.csv
#### Columns:
  1. cntrb_id
  2. repo_id
  3. action
  4. action_year
  5. action_quarter
  6. counter

## Metadata
For each respository we have metadata that may be interesting and useful.
### repo_info.csv
There is a lot of information in here, and most of it is not essential for analysis we might perform, or visualizations we might create. Specifically, the repo_id value will map to the repo_id values in the network data sets. The repo_git will map to the repository's location on GitHub. This repo_git (which is a url) can be parsed to identify which repositories exist as part of which CNCF projects. 
#### Columns:
  1. **repo_id**
  2. repo_group_id
  3. **repo_git**
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
This is a map of repository IDs to CNCF category: Sandbox, Incubating, or Graduated. 
#### Columns:
  1. repo_id
  2. category

## action_types.csv
A list of the 13 possible action types note above. 
#### Columns:
  1. action

