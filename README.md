# Fringe Generator

This little project is used to generate a fringe pattern.

## Requirements

File "requirements.txt" contains the minimum needed python packages.

It is recommended to use a virtual environment to execute this project.

```python
   python -m venv <virutal environment name>
   source <virutal environment name>/bin/activate
```

## Usage

To execute this project, run:

```python
    python main_fringeGenerator.py -conf parameters.yaml
```

- The "parameters.yaml" file contains the needed parameter to configure the output fringe pattern

| Parameter         | Type    | Description                                                                                       |
| :---------------- | :------ | :------------------------------------------------------------------------------------------------ |
| `initial_phase`   | `float` | Indicates the initial fringe phase (commonly set to 0).                                           |
| `initial_period`  | `float` | Indicates the size of the fringe. The larger the value, the wider the fringe.                     |
| `delta_phase_deg` | `float` | Indicates the phase shift.                                                                        |
| `vertical_fringe` | `bool`  | Used to indicates the fringe orientation (True -> verticla fringes. False -> horizontal fringes). |
| `width`           | `int`   | Fringe image widht. Note: Use the montor width resolution.                                        |
| `height`          | `float` | Fringe image height Note: Use the montor height resolution.                                       |
| `fps`             | `int`   | the frequency at which it will change from one pattern to another.                                |

- Once the code is running, it is possible to change the fringe pattern:

| Key           | Description                                           |
| :------------ | :---------------------------------------------------- |
| `right arrow` | Increase the fringe width                             |
| `left arrow`  | Decreases the fringe width                            |
| `s`           | Start/stop the fringe motion                          |
| `f`           | Shifts the pattern according to the delta phase value |

Note. When key 'f' is used, the pattern is shifted up to three times. This is usefull for 4 phase shifting analysis.

## Author

- [@luismvc](https://github.com/luismvc)
