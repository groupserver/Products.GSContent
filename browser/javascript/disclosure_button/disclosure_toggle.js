// Functions for handling the disclosure buttons.
var disclosureHiddenArrow = "\u25b6";
var disclosureShownArrow = "\u25bc";
var disclosureNBSP = "\u00a0";

function showHideDisclosure(widget)
{
    var w = $(widget);
    setToggleArrow(w);
    showhide = w.getElementsByClassName('disclosureShowHide')[0];
    Effect.toggle(showhide, 'blind', {duration: 1, delay: 0});
}

function addArrowsToDisclosureButtons()
{
    var i = 0;
    widgets = document.getElementsByClassName('disclosureWidget');
    for (i=0; i< widgets.length; i++)
    {
        button = widgets[i].getElementsByClassName('disclosureButton')[0];
        addHiddenArrowToElement(button);
    }
}

function setToggleArrow(w)
{
    button = $(w).getElementsByClassName('disclosureButton')[0];
    if (widgetHidden(w))
    {
        addShownArrowToElement(button);
    }
    else
    {
        addHiddenArrowToElement(button);
    }
}

function widgetHidden(widget)
{
    var retval = true;
    var w = $(widget);
    var showhide = w.getElementsByClassName('disclosureShowHide')[0];
    var showhideDisplay = showhide.getStyle('display');
    retval = (showhideDisplay == 'none');
    return retval;
}

function addShownArrowToElement(element)
{
    var e = $(element);
    var text  = getRealText(e.childNodes[0].data);
    e.childNodes[0].data = disclosureShownArrow + disclosureNBSP + text;
}

function addHiddenArrowToElement(element)
{
    var e = $(element);
    var text  = getRealText(e.childNodes[0].data);
    e.childNodes[0].data = disclosureHiddenArrow + disclosureNBSP + text;
}

function getRealText(text)
{
    var retval = '';
    c0 = text.charAt(0);
    if ((c0 == disclosureHiddenArrow) || (c0 == disclosureShownArrow))
    {
        retval = text.substring(2, text.length);
    }
    else
    {
        retval = text;
    }
    return retval;
}

/* Add the disclosure buttons to the widgets after the page has loaded */
Event.observe(window, 'load', addArrowsToDisclosureButtons);

