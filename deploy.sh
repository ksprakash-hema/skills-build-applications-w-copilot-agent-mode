#!/bin/bash
cd /workspaces/skills-build-applications-w-copilot-agent-mode
git checkout -b build-octofit-app
git add octofit-tracker/frontend/
git commit -m "Add React frontend with API components for OctoFit Tracker"
git push -u origin build-octofit-app
