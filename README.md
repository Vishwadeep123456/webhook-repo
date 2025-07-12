# webhook-repo
 GitHub Webhook Receiver – Flask + MongoDB

This repository contains the backend server that receives GitHub webhook events (Push and Pull Request), stores them in MongoDB, and serves them via an API with a minimal frontend UI.

---

 Tech Stack

 Flask (Python)
 GitHub Webhooks
 MongoDB Atlas (Cloud)
 Deployed on Render

---

 Features

 Handles `push` and `pull_request` events from GitHub
 Extracts author, branch info, and timestamp
 Stores the events in MongoDB with clean formatting
 Exposes a `/events` API endpoint
 Frontend polls the API every 15 seconds and displays the latest events

---

Event Format Examples

 PUSH
