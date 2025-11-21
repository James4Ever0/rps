# RPS

Request-based Process Scheduler

## Description

RPS is a request-based process scheduler that can be used to schedule processes based on their network request priorities. It is designed to be used in a multi-process environment where processes need to be scheduled within limited hardware resources, like VRAM, RAM and disk size.

## Features

- Onhold requests which do not have corresponding process to handle
- Priority queue for requests, batch handle nearby requests with same target process
- Process resource estimation based on heuristics
- Established connection based active process detection