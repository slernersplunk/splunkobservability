# terraform-provider-signalfx

[![Changelog](https://img.shields.io/badge/changelog-right%20here-blue.svg)](https://github.com/signalfx/terraform-provider-signalfx/blob/master/CHANGELOG.md)
[![Build Status](https://travis-ci.org/signalfx/terraform-provider-signalfx.svg?branch=master)](https://travis-ci.org/signalfx/terraform-provider-signalfx)

This is a [Terraform](https://www.terraform.io/) provider to codify [SignalFx](http://signalfx.com) detectors, charts and dashboards, thereby making it easier to create, manage and version control them.

This provider was originally created and maintained by [Yelp](https://www.yelp.com/engineering) for years before being taken over as an official SignalFx project. It also contains contributions from a fork maintained by [Stripe](https://stripe.com/). Thanks, folks to Yelp and Stripe for their work!

* Resources
    * [Detector](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/detector.md)
    * [Chart](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/chart.md)
        * [Time Chart](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/time_chart.md)
        * [List Chart](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/list_chart.md)
        * [Single Value Chart](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/single_value_chart.md)
        * [Heatmap Chart](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/heatmap_chart.md)
        * [Text Note](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/text_note.md)
        * [Event Feed](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/event_feed_chart.md)
    * [Dashboard](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/dashboard.md)
    * [Dashboard Group](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/dashboard_group.md)
    * [Integration](https://github.com/signalfx/terraform-provider-signalfx/blob/master/docs/resources/integration.md)
* [Build And Install](#build-and-install)
    * [Build binary from source](#build-binary-from-source)
* [Release](#release)
* [Contributing](#contributing)
* [Conversion from SignalForm](#conversion-from-signalform)
* [FAQ](#faq)

## Configuration

This provider has the following configuration options:

* `auth_token` (required) - The auth token for [authentication](https://developers.signalfx.com/basics/authentication.html)
* `api_url` - The API URL to use for communicating with SignalFx. This is helpful for organizations who need to set their Realm or use a proxy.
 Note: You likely want to change `custom_app_url` too!
* `custom_app_url` - The application URL that users should use to interact with assets in the browser. This is used by organizations using specific realms or those with a custom [SSO domain](https://docs.signalfx.com/en/latest/admin-guide/sso.html).

## Build And Install

### Build binary from source

To build the go binary from source:

```bash
go build
```

The output binary will be named `terraform-provider-signalfx`.

If you want to customize your target platform set the `GOOS` and `GOARCH` environment variables; e.g.:
```bash
GOOS=darwin GOARCH=amd64 make build
```

Once you have built the binary, place it in the your terraform installation for it to be available everywhere. For local use, this is usually `~/.terraform.d/plugins`.

## Release

To make a new release:

1. Decide on the next version, use [semantic versioning](https://semver.org/)
1. Edit `CHANGELOG.md` and make sure all the goodies are in it!
1. `git commit`
1. `git tag v<VERSION>`
1. `git push origin master && git push origin --tags`

## Contributing
Everyone is encouraged to contribute to `terraform-provider-signalfx`. You can contribute by forking the GitHub repo and making a pull request or opening an issue.

## Running tests

To run the tests, run `go test ./...`

## Conversion From SignalForm

This provider because the official SignalFx provider at the time of [SignalForm](https://github.com/Yelp/terraform-provider-signalform) v2.8.0. Conversions from SignalForm to this module at that point in time have no compatibility issues.

To perform a conversion you'll need to do two things:
* adjust the provider configuration
* change Terraform configuration files to references the new provider name
* update state files to reference the new provider name

Each are easy to do! You'll need to do them at the same time, however, avoiding any asset changes between each step.

### Adjust Provider Configuration

The SignalForm provider is configured like:

```
provider "signalform" {
  auth_token = "XXX"
}
```

You'll need to change the name from `signalform` to `signalfx` wherever you've set this up in your file layout.

### Changing Terraform Configuration

This should be a straight-forward search and replace, but please mind that you may have some naming conventions in your install for which the following instructions don't work. Double check everything!

All of the SignalForm resources look like `signalform_…`. You'll want to search and replace this string with `signalfx_…"`. You can do this in a code editor or on the command line with something like:

* OS X: `find . -regex ".*\.tf" -type f -exec sed -i '' 's/signalform_/signalfx_/' {} +`
* GNU `sed`, like Linux: `find . -regex ".*\.tf" -type f -exec sed -i s/signalform_/signalfx_/' {} +`

This should handle replacing all resource definitions as well as references to those resources.

To cap it off, run `terraform init`.

### Update State Files

First, make a backup of your state file just in case.

Note: Terraform state files are [friendly to command lines](https://www.terraform.io/docs/commands/state/index.html#command-line-friendly). You may choose another way to migrate that doesn't use `terraform state mv` and instead modifies the file directly. Using the process below fits Terraform's advice wherein they "we recommend piping Terraform state subcommands together with other command line tools". It also works with remote state files.

The state files in Terraform now need to be updated to use the new provider name. We can first find a list of all resources in the state file:

```
$ terraform state list
signalform_dashboard.mydashboard0
signalform_dashboard_group.mydashboardgroup0
signalform_time_chart.mychart0
```

Just like our configuration, we're just changing `signalform_` to `signalfx_`. Here's a bit of Bash to do that (remove the wrapping `echo` to run it):

```
#!/bin/bash

for resource in $(terraform state list); do
  if [[ $resource == *"signalform_"* ]]; then
    newresource=$(echo $resource | sed 's/signalform_/signalfx_/')
    echo "terraform state mv $resource $newresource"
  fi
done
```

When run, you should see something like:

```
Moved signalform_dashboard.mydashboard0 to signalfx_dashboard.mydashboard0
Moved signalform_dashboard_group.mydashboardgroup0 to signalfx_dashboard_group.mydashboardgroup0
Moved signalform_time_chart.mychart0 to signalfx_time_chart.mychart0
```

After that we can run a `terraform plan` to ensure everything is unchanged:

```
…
No changes. Infrastructure is up-to-date.
…
```

## FAQ

**What is SignalForm?**

Yelp helpfully created and maintained this provider for years, then allowed SignalFx to take it over as our official provider. Thanks, Yelp! This provider was called SignalForm then. You should use this one now!

**Can I use the UI to help me?**

Sure! Any given a chart or detector created from the UI, you can see its representation in Signalflow from the Actions menu:

![Show SignalFlow](https://github.com/signalfx/terraform-provider-signalfx/raw/master/docs/show_signalflow.png)
![Signalflow](https://github.com/signalfx/terraform-provider-signalfx/raw/master/docs/signalflow.png)
