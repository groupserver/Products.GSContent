function showHideDisclosure(remainderId, discloseButtonId, text)
{
    var hiddenArrow = "\u25b6";
    var shownArrow = "\u25bc";
    var nbsp = "\u00a0";
    var discloseElement = document.getElementById(discloseButtonId);
    if (discloseElement.childNodes[0].data.substring(0,1) == shownArrow)
    { 
        discloseElement.childNodes[0].data = hiddenArrow + nbsp + text;
    }
    else
    {
        discloseElement.childNodes[0].data = shownArrow + nbsp + text;
    }
    Effect.toggle(remainderId,'blind', {duration: 1, delay: 0});
}

