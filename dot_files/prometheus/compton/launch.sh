#!/usr/bin/env bash

# Terminate already running bar instances
killall compton

sleep 1

# Launch compton
compton --config config &
