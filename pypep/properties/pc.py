
# -*- coding: utf-8 -*-
def BrooksCorey(sw,pt,a,swr,snwr=0):
    r"""
    Computes capillary pressure using the Brooks-Corey model $f^3$
    
    .. math::
    p_c = \left( \frac{1-s_{wr}-s_{wnr}}{s_w - s_{wr}} \right)
    
    Parameters
    ----------
    sw : array
        The water saturation values
    pt : float
        The entry pressure value
    a : float
        The index that describes the distribution of pore sizes
    swr : float
        The saturation value of the residual wetting phase
    snwr : float, optional
        TThe saturation value of the residual non-wetting phase
    
    Returns
    -------
    out : Array
        Array of capillary pressure values of given sw, pt, a, swr, and snwr.
    """
    se = (1-swr-snwr)/(sw-swr)
    pc = pt*((se)**(1/a))
    
    return pc