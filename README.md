# Time Justice — Community Transit Scheduler

**An interactive Python prototype for exploring public transit service frequency and basic accessibility indicators.**

Developed as a final project for **Stanford Code in Place** by Beste Bozkurt.

[View the original Stanford Code in Place project](https://codeinplace.stanford.edu/cip6/share/7H9UcMwhPzZDMbEkZaCv)

## Project motivation

Public transit quality is not only about network efficiency: service frequency and physical accessibility can shape people's opportunities to move through a city. This educational prototype explores how a planner might inspect and adjust those service attributes in a simple, interactive environment.

## What the program does

- Displays five example transit routes, including their corridor, service headway (minutes between vehicles), and binary accessibility status.
- Calculates the proportion of routes marked accessible and counts routes with headways of 10 minutes or less.
- Allows users to update a route's headway and accessibility status during the current session and rerun the summary.

## How to run

Requires **Python 3**. No external packages are needed.

```bash
python3 time_justice.py
```

Select options `1`–`4` in the terminal. To update a route, enter its name exactly as displayed.

## Example baseline results

The included illustrative five-route network produces:

| Indicator | Baseline |
| --- | ---: |
| Routes evaluated | 5 |
| Routes marked accessible | 3 of 5 (60%) |
| Routes with headway ≤ 10 minutes | 2 of 5 |

These are **route-level descriptive indicators**, not population-weighted measures of accessibility or transportation equity.

## Methods and limitations

The network is a small, manually defined example rather than an imported GTFS or observed transit dataset. The accessibility field is binary and does not capture detailed station, vehicle, sidewalk, or trip accessibility. The program does not calculate travel-time accessibility, actual passenger waiting times, demographic disparities, or causal equity impacts. Its statement about burdens on vulnerable commuters is a planning hypothesis presented for reflection, **not a finding established by this example dataset**.

Updates are held in memory only and are not saved after the program exits. The current educational version expects an integer when editing headways and does not validate positive values or all accessibility responses.

## Potential next steps

Future development could incorporate real transit schedule data, spatial accessibility measures, and demographic context, then compare service scenarios using explicit equity metrics. These are **proposed extensions**, not features of the current prototype.

## Academic context

This project connects an urban and regional planning background with introductory Python programming and an interest in transportation accessibility, time justice, and computational planning methods.
