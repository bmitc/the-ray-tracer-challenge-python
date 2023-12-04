# pylint: disable=W,C,R

# This script will display a project being shot out at an initial velocity
# and its trajectory. The projectile is displayed as a green pixel.
#
# Run this script via:
# ```
# poetry run projectile
# ```

from ray_tracer_challenge.tuples import *
from ray_tracer_challenge.color import *
from ray_tracer_challenge.canvas import *


class Projectile:
    def __init__(self, position: Point, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity


class Environment:
    def __init__(self, gravity: Vector, wind: Vector) -> None:
        self.gravity = gravity
        self.wind = wind


def tick(environment: Environment, projectile: Projectile) -> Projectile:
    return Projectile(
        projectile.position + projectile.velocity,
        projectile.velocity + environment.gravity + environment.wind,
    )


initial_position = Projectile(Point(0, 1, 0), 11.25 * (Vector(1.0, 1.8, 0).normalize()))

initial_environment = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))


def run(environment: Environment, initial_position: Projectile, canvas: Canvas) -> None:
    projectile = initial_position
    while tick(environment, projectile).position.y >= 0.0:
        projectile = tick(environment, projectile)
        canvas.set_pixel(
            round(projectile.position.x),
            canvas.height - round(projectile.position.y),
            Colors.GREEN.value,
        )
    canvas.show()


def projectile() -> None:
    run(initial_environment, initial_position, Canvas(900, 550))
