# SSM Parameter Store Manager

Get and set parameters stored in AWS SSM.

## Installation

Install latest version:

```
pip install git+https://git@github.com/craighurley/ssmpsm.git
```

Install specific version:

```
pip install git+https://git@github.com/craighurley/ssmpsm.git@1.0.0
```

## Usage

```
Usage:
    ssmpsm get [-s] [-p AWS_PROFILE]
    ssmpsm set FILE [-d] [-p AWS_PROFILE]
    ssmpsm (-h | --help)
    ssmpsm (-v | --version)

Arguments:
    get           Get parameters.
    set           Create/update/delete parameters.
    FILE          Path to file that contains parameters.

Options:
    -d            Perform a dryrun.
    -h --help     Show this screen.
    -p PROFILE    AWS profile to use.
    -s            Get secret value.
    -v --version  Show version.
```

### FILE Format

`ssmpms` determines what to do with an entry based on the first character(s).  Examples work best to describe the options:

```
/create/string=foo
-/delete/string=bar
*/create/securestring=password
!/create/string/but/do/not/update=foo
!*/create/securestring/but/do/not/update=bar
-!*/delete/securestring=
```

## Development

```sh
pip install -r requirements
```

## Links

- <https://docs.aws.amazon.com/cli/latest/reference/ssm/>
