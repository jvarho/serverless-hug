serverless-hug
===

Example to show how to run [hug][1] in AWS lambda using [serverless][2].

Steps to install and test:

1. `nvm install` or `nvm use` (if your default node is incompatible)

2. `npm install`

3. `npm run sls-serve`

This starts a local test server. You can test against it using:

    curl -H 'X-Who: Steve' http://localhost:5000/hello

To deploy to AWS use `npm run sls-deploy`.
That requires AWS credentials configured.
For deployed URL, see the output of sls-deploy.

[1]: https://www.hug.rest/
[2]: https://serverless.com/
