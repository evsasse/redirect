# Redirect

Redirect a subdomain to somewhere else that contains a path,
eg. `curriculum.my-name.com` -> `linkedin.com/my-name`

## Why?

Because it's not possible to redirect to a specific path on the DNS level.

## To make a new domain redirect:

- Create a new custom domain for it on the API Gateway that Zappa creates for you. This will also create an alias on AWS for this resource, something like `bs34ub367pbtw.cloudfront.net.`.

- Create an A record on Route53 pointing to this new alias.

- Modify the `domains.json` file to redirect the new domain to your preferred location.

- Deploy it.

- The DNS configuration may need a couple minutes to work.
  But if takes more than 5 minutes, something is probably wrong.
