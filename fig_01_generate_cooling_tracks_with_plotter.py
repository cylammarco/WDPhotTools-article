import os

from WDPhotTools import plotter


try:

    HERE = os.path.dirname(os.path.realpath(__file__))

except Exception as e:

    print(e)
    HERE = os.path.dirname(os.path.realpath(__name__))

plotter.plot_atmosphere_model(
    invert_yaxis=True,
    savefig=True,
    folder=".",
    filename="fig_01_DA_cooling_tracks_from_plotter",
    ext=['png', 'pdf'],
)
