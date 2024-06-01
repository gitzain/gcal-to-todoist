# gcal-to-todoist
This script enables users to automatically transfer events from their Google Calendar to their Todoist task list, enhancing productivity and task management efficiency.


## Table of content
- [Motivation](#motivation)
- [Installation & Usage](#installation--usage)
    - [Installation](#installation)
    - [Usage](#usage)
- [Contributing](#contributing)
- [History](#history)
- [Credits](#credits)
- [License](#license)


## Motivation
This script bridges the gap between time management and task tracking by automatically transferring events from Google Calendar to Todoist. While calendars help manage time, to-do lists track actionable tasks. This integration allows users to seamlessly convert scheduled events into actionable to-do list items, ensuring tasks are tracked and completed efficiently. It streamlines workflow by eliminating the need to manually duplicate calendar events as to-do list tasks, thereby improving productivity and organization.


## Installation & Usage
You're right, typically the `main.yaml` file in the `.github/workflows` directory doesn't need to be edited if it's already configured correctly. Let me revise the instructions accordingly:

## Installation & Usage

### Installation
1. Fork this repository [gcal-to-todoist](https://github.com/gitzain/gcal-to-todoist) to your GitHub account.

### Usage
1. Ensure your repository has the following secrets set up:
   - `GOOGLE_SERVICE_KEY`: Contents of your Google service account key JSON file.
   - `GOOGLE_CALENDAR_ID`: Google Calendar ID.
   - `TODOIST_API_TOKEN`: Todoist API token.
   - `TODOIST_PROJECT_ID`: Todoist project ID.

2. Enable the workflow:
   - The workflow is set to run daily at 00:01 by default (`1 0 * * *`).
   - Navigate to the "Actions" tab in your GitHub repository.
   - Select "Sync Calendar to Todoist" under the list of workflows.
   - Click the "Run workflow" button to manually trigger the workflow.

3. Check your Todoist project:
   - Open Todoist to see the events from Google Calendar now listed as tasks.
   - You can manage these tasks as usual in Todoist, including marking them as complete.

4. Customize the automation:
   - If you need to modify the schedule or any other aspect of the automation:
     - Open the `.github/workflows/main.yaml` file.
     - Edit the file to make necessary changes (e.g., adjusting the schedule, modifying the Python version, etc.).
     - Commit the changes to apply the modifications.


## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Added some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## History
26/01/24: v1 published to github. 


## Credits
- Created by <a href="https://iamzain.com">Zain Khan</a>.
- Template for this README is <a href="https://github.com/gitzain/template-README">Template-README</a> created by <a href="https://iamzain.com">Zain Khan</a>


## License
See the LICENSE file in this project's directory.
