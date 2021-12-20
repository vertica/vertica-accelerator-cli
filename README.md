
(c) Copyright 2021 Micro Focus or one of its affiliates

# Vertica Accelerator Command Line Client #

The Vertica Accelerator Command Line Interface (VCLI) is an alternate client for managing Vertica Accelerator databases.

- [Vertica Accelerator Command Line Client](#vertica-accelerator-command-line-client)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Installing the latest release](#installing-the-latest-release)
    - [Installing from source](#installing-from-source)
    - [Autocomplete](#autocomplete)
  - [Package release process](#package-release-process)
  - [Post-install Configuration](#post-install-configuration)
  - [Context-sensitive help](#context-sensitive-help)
  - [Maintainers](#maintainers)

## Prerequisites
* You must be customer or trial user of Vertica Accelerator with a valid account to use VCLI.
* You can contact the project maintainers or Vertica Accelerator support to obtain a "accelerator_client_id" which is needed in order to use the package 

## Installation
### Installing the latest release
  ```
  $ pip3 install vertica-accelerator-cli
  ```
  or
  ```
  $ python3 -m pip install dist/vertica-accelerator-cli-0.1.0.tar.gz --upgrade
  ```
### Installing from source
  ```
  $ pip3 install git+https://github.com/vertica/vertica-accelerator-cli.git@master
  ```

### Autocomplete
  To enable autocomplete for VCLI, install and configure argcomplete:
  ```
  $ sudo python3 -m pip install argcomplete
  $ sudo activate-global-python-argcomplete
  ```

## Package release process
1. Create a virtual environment:
  ```
  $ python3 -m venv env
  $ source venv/bin/activate
  $ export PYTHONPATH=.
  $ mkdir ./python-packages/
  ```
2. Create the package:
  ```
  $ python3 -m pip install --upgrade build
  $ python3 -m build
  ```
 

## Post-install Configuration
You can create profiles to manage multiple identities.

1. Run the interactive configuration to create a new profile called `accelerator-profile`:
  ``` 
  $ va config --profile accelerator-profile
  ```

2. You must log in to a profile with `va login --profile` to execute VCLI commands. Logins expire in one hour. For help, run `va login -h`:
  ```
  $ va login --profile accelerator-profile
  Login success
  ```

3. Create a file `~/.vcli/credentials` with the following format:
  ```
  [default]
  username = example@example.com
  password = example_password
  client_id = example_client_id
  auth_endpont = https://vertica.okta.com
  access_token_file = sample_access_token
 
  [accelerator-profile]
  username = accelerator-profile@domain.com
  password = accelerator-profile_password
  client_id = accelerator_client_id
  auth_endpont = https://vertica.okta.com
  access_token_file = accelerator-profile_access_token
  ```
  
4. Create a file `~/.vcli/config` with the following format:
  ```
  [default]
  service_endpoint = https://accelerator.vertica.com
  max_attempts = 3

  [vaas-test]
  service_endpoint = https://accelerator.vertica.com
  max_attempts = 3
  verify_ssl=false
  ```


## Context-sensitive help
For help, run `va --help` or `va -h`:
  ```
  $ va --help
  usage: va [-h] {config,login,logout,database,database-config,subcluster,backup,session,task,cron,report,dns}

  Vertica Command Line Interface (VCLI) is a tool to manage Vertica Accelerator databases.

  positional arguments:
    {config,login,logout,database,database-config,subcluster,backup,session,task,cron,report,dns}
      config              Configure VCLI to access Vertica Accelerator.
      login               Log in to Vertica Accelerator.
      logout              Log out from Vertica Accelerator.
      database            Manage the Database.
      database-config     Manage the Database Configuration.
      subcluster          Manage subclusters.
      backup              Backup and restore the database.
      session             Manage sessions.
      task                Manage tasks.
      cron                Manage the scheduler.
      report              Show and generate reports.
      dns                 Manage DNS.

  optional arguments:
    -h, --help            show this help message and exit
  ```
  
You can also run ``--help`` or `-h` after any positional argument for details on that particular argument.

* To view `va database` options:
  ```
  $ va database -h
  usage: va database [-h] {create,list,get,start,stop,hibernate,revive,drop,increase,decrease,rescale,upgrade,update-network-config}

  positional arguments:
    {create,list,get,start,stop,hibernate,revive,drop,increase,decrease,rescale,upgrade,update-network-config}
      create                 Create a new database.
      list                   View a list of the databases and their properties.
      get                    View details of a particular database and its subclusters.
      start                  Start the database.
      stop                   Stop the database.
      hibernate              Hibernate the database.
      revive                 Revive the database.
      drop                   Drop an existing database.
      increase               Increase the number of nodes for the database.
      decrease               Decrease the number of nodes for the database.
      rescale                Change the instance type of the nodes.
      upgrade                Upgrade a database.
      update-network-config  Update the external access CIDR block.

  optional arguments:
    -h, --help            show this help message and exit
  ```
  
* To view `va database create` options:
  ```
  $ va database create -h
  usage: va database create [-h] --name <value> --password <value> --nodes <value>
                                 --region <value> --availability_zone <value> 
                                 --instance_type <value> [--external_access_cidr_block <value>]
                                 [--vertica_version <value>] [--profile <value>]

  optional arguments:
    -h, --help            show this help message and exit
    --name <value>        The name of the database. The database name must consist of
                          1 to 18 alpha-numeric characters and start with a letter.
    --password <value>    The password for the database. The password must consist of
                          8 to 30 upper-case, lower-case, numeric, and special characters.
    --nodes <value>       The number of primary cluster nodes for the database. Valid values: [3, 6, 12]
    --region <value>      The region of the database. For example: 'us-east-1'
    --availability_zone <value>
                          The availability zone of the database. For example: 'us-east-1a'
    --instance_type <value>
                          The instance type of the database. 
                          Valid values: ['i3.2xlarge', 'i3.4xlarge', 'i3.8xlarge', 'i3.16xlarge']
    --external_access_cidr_block <value>
                          The IPv4 external access CIDR block(s) of the database, which acts as a whitelist
                          for a range of IP addresses that can access the database as a client. For example,
                          the CIDR block 192.0.2.0/24 allows clients to connect from 192.0.2.0 through 192.0.2.255.
                          Separate multiple CIDR blocks with a comma: 192.0.2.0/24,192.0.2.0/32
    --vertica_version <value>
                          The AMI version of the Vertica database. Valid values: ['10.1.0-1', '10.1.0-2', '11.0.0-1']
    --profile <value>     Use a specific profile from the credentials file (default path: "~/.vcli/credentials").
                          If you don't specify a profile, VCLI defaults to the 'default' profile when
                          communicating with Vertica Accelerator services.
  ```

## Maintainers
* Hao Yang
* Xiaojing He
* Kirtan Chavda
* Sumeet Keswani

