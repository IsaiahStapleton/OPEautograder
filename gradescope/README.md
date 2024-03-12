# Setup

Set the environmental variables in [`run_autograder`](run_autograder) to match your OpenShift API configuration from [`autograder.env`](../manifests/autograder.env).

- `LINK` -- link to your OpenShift route 
  - *you can get this link by running `oc describe route/autograder-route | grep Requested`*
- `USERNAME` -- username configured for API
- `PASSWORD` -- password configured for API
- `ASSIGNMENT_NAME` -- name for directory of assignment that you are grading from your private autograder repo

Then run `./zip.sh` to create `autograder.zip` which you will upload as input for your [gradescope container](https://gradescope-autograders.readthedocs.io/en/latest/getting_started/).
