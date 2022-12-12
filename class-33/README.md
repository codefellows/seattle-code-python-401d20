# Authentication & Production Server

## Overview

We've restricted actions based on a user's status. But how do we know that a user is who they claim to be?

For that we need `Authentication`. There are lots of ways to authenticate. We will be using JSON Web Token authentication.

We've recently moved to a production-grade database. But how about the server? Today we'll move beyond Django's built in development server to a "real" server - Gunicorn.

## Class Outline

<!-- To Be Completed By Instructor -->

## Learning Objectives

### Students will be able to

#### Describe and Define

- Difference between Authorization and Authentication
- Role of a production server
- How JSON Web Tokens work

#### Execute

- Integrate Gunicorn into Docker container
- Request and refresh authentication tokens
- Modify Django's default authentication classes
