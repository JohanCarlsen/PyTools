def set_size(width: str='col', scale: float=1.0,
             subplot: tuple=(1, 1)) -> tuple:
    r'''
    Set the size of a figure where the height/wifdth equals the golden ratio.

    Parameters
    ----------
    width : {'col', 'text'} or `float`, optional 
        Width of the figure in pts. Possible values:

            * 'col' (default): 255.46837
            * 'text' : 528.93675

    scale : `float`, default: 1.0
        How to scale the height of the figure, ie. `figsize=(width, height * scale)`

    subplot : `tuple`, default: (1, 1)
        How to scale the figure size based on the number of subplots:
        `figsize=(width, height * subplot[0] / subplot[1])`

    Returns
    -------
    tuple
        Dimension of the figure, ie. `(width, height * scale * subplot[0] / subplot[1])`

    Notes
    -----
        The built-in values for `width` and `height` are the column width and text width
        in REVTeX document class. To obtain the appropriate values for your document, 
        run the commands `\the\columnwidth` and `\the\textwidth` in your document body.
    '''
    widths = {
        'col': 255.46837,
        'text': 528.93675
    }

    if width in widths:
        width_pt = widths[width]
    
    else:
        width_pt = width
    
    ratio = (5**0.5 - 1) / 2
    fig_width = width_pt / 72.27
    fig_height = fig_width * ratio * scale * subplot[0] / subplot[1]
    fig_dims = (fig_width, fig_height)

    return fig_dims