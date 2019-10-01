#!/bin/bash
mydir=$(dirname "$0")
source $mydir/../.env

tensorboard --logdir=reports/models/