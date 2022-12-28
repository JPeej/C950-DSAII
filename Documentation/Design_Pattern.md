This is design pattern version 1.0 for the C950 project. Version 1.0 is a 
brainstorm of what packages I will need to build, their attributes and methods, 
and what the pseudocode of main will be.  Version 1.1 will include pseudocode 
of each package's methods.

# Packages

## Truck
### Attributes
    -   speed (CONSTANT?)
    -   driver
    -   location
    -   mileage
    -   packages
    -   capacity (CONSTANT?)
    -   current_load
### Methods
    -   drive_to
    -   get_location
    -   swap_driver
    -   load_packages
    -   deliver_package

## Package
### Attributes
    -   id
    -   address
    -   city
    -   zip
    -   deadline
    -   weight
    -   status
### Methods
    -   set_status

## Hashtable
### Attributes
    -   capacity
    -   list
### Methods
    -   insert
    -   remove
    -   lookup


# Main Pseudo Code
    -   Initiate hash table
    -   Read package csv 
            Create package object with read data
            Create hash with package object
            Insert package into hash table
    -   Read distance csv
            Save distance data for algo use
    -   Initiate truck 1 with packages
    -   Initiate truck 2 with packages
    -   Initiate truck 3 with packages
        