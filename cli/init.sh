#!/usr/bin/bash


echo "Add git safe directory"
git config --global --add safe.directory /workspaces/pl-platform-api

echo "Installing requirements"
pip install -r requirements.txt