from typing import Any, List

from typing import overload


class XLCell:
    def __init__(self, *args, **kwargs) -> None: ...

    def cellReference(self, *args, **kwargs) -> Any: ...

    def formula(self) -> str: ...

    def hasFormula(self) -> bool: ...

    def setFormula(self, arg0: str) -> None: ...

    def value(self, *args, **kwargs) -> Any: ...

    def valueType(self, *args, **kwargs) -> Any: ...


class XLCellRange:
    def __init__(self, *args, **kwargs) -> None: ...

    def begin(self, *args, **kwargs) -> Any: ...

    def clear(self) -> None: ...

    def end(self, *args, **kwargs) -> Any: ...

    def numColumns(self) -> int: ...

    def numRows(self) -> int: ...


class XLCellReference:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg0: str) -> None: ...

    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...

    @overload
    def __init__(self, arg0: int, arg1: str) -> None: ...

    @overload
    def __init__(*args, **kwargs) -> Any: ...

    def address(self) -> str: ...

    def column(self) -> int: ...

    def row(self) -> int: ...

    def setAddress(self, arg0: str) -> None: ...

    def setColumn(self, arg0: int) -> None: ...

    def setRow(self, arg0: int) -> None: ...

    def setRowAndColumn(self, arg0: int, arg1: int) -> None: ...


class XLCellValue:
    def __init__(self, *args, **kwargs) -> None: ...

    def asString(self) -> str: ...

    def clear(self) -> None: ...

    def valueType(self, *args, **kwargs) -> Any: ...

    @property
    def booleanValue(self) -> Any: ...

    @booleanValue.setter
    def booleanValue(self, val: Any) -> None: ...

    @property
    def floatValue(self) -> Any: ...

    @floatValue.setter
    def floatValue(self, val: Any) -> None: ...

    @property
    def integerValue(self) -> Any: ...

    @integerValue.setter
    def integerValue(self, val: Any) -> None: ...

    @property
    def stringValue(self) -> Any: ...

    @stringValue.setter
    def stringValue(self, val: Any) -> None: ...

    @property
    def value(self) -> Any: ...

    @value.setter
    def value(self, val: Any) -> None: ...


class XLChartsheet:
    def __init__(self, *args, **kwargs) -> None: ...

    def clone(self, arg0: str) -> None: ...

    def color(self, *args, **kwargs) -> Any: ...

    def index(self, arg0: int) -> None: ...

    def isSelected(self) -> bool: ...

    def name(self) -> str: ...

    def setColor(self, arg0) -> None: ...

    def setIndex(self, arg0: int) -> None: ...

    def setName(self, arg0: str) -> None: ...

    def setSelected(self, arg0: bool) -> None: ...

    def setVisibility(self, arg0) -> None: ...

    def visibility(self, *args, **kwargs) -> Any: ...


class XLColor:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...

    @overload
    def __init__(self, arg0: str) -> None: ...

    @overload
    def __init__(*args, **kwargs) -> Any: ...

    @overload
    def blue(self) -> int: ...

    @overload
    def blue(self) -> str: ...

    @overload
    def blue(*args, **kwargs) -> Any: ...

    def green(self) -> int: ...

    @overload
    def red(self) -> int: ...

    @overload
    def red(self) -> int: ...

    @overload
    def red(*args, **kwargs) -> Any: ...

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> None: ...

    @overload
    def set(self, arg0: str) -> None: ...

    @overload
    def set(*args, **kwargs) -> Any: ...


class XLColumn:
    def __init__(self, *args, **kwargs) -> None: ...

    def isHidden(self) -> bool: ...

    def setHidden(self, arg0: bool) -> None: ...

    def setWidth(self, arg0: float) -> None: ...

    def width(self) -> float: ...


class XLDocument:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, filename: str) -> None: ...

    @overload
    def __init__(*args, **kwargs) -> Any: ...

    def close(self) -> None: ...

    def create(self, filename: str) -> None: ...

    def deleteProperty(self, property) -> None: ...

    def name(self) -> str: ...

    def open(self, filename: str) -> None: ...

    def path(self) -> str: ...

    def property(self, property) -> str: ...

    def save(self) -> None: ...

    def saveAs(self, filename: str) -> None: ...

    def setProperty(self, property, value: str) -> None: ...

    def workbook(self, *args, **kwargs) -> Any: ...


class XLProperty:
    AppVersion: Any = ...
    Application: Any = ...
    Category: Any = ...
    Company: Any = ...
    CreationDate: Any = ...
    Creator: Any = ...
    Description: Any = ...
    DocSecurity: Any = ...
    HyperlinkBase: Any = ...
    HyperlinksChanged: Any = ...
    Keywords: Any = ...
    LastModifiedBy: Any = ...
    LastPrinted: Any = ...
    LinksUpToDate: Any = ...
    Manager: Any = ...
    ModificationDate: Any = ...
    ScaleCrop: Any = ...
    SharedDoc: Any = ...
    Subject: Any = ...
    Title: Any = ...
    __entries: Any = ...

    def __init__(self, arg0: int) -> None: ...

    def __eq__(self, other) -> Any: ...

    def __getstate__(self) -> Any: ...

    def __hash__(self) -> Any: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __ne__(self, other) -> Any: ...

    def __setstate__(self, state) -> Any: ...

    @property
    def name(self) -> Any: ...

    @property
    def __doc__(self) -> Any: ...

    @property
    def __members__(self) -> Any: ...


class XLRow:
    def __init__(self, *args, **kwargs) -> None: ...

    def cellCount(self) -> int: ...

    def descent(self) -> float: ...

    def height(self) -> float: ...

    def isHidden(self) -> bool: ...

    def rowNumber(self) -> int: ...

    def setDescent(self, arg0: float) -> None: ...

    def setHeight(self, arg0: float) -> None: ...

    def setHidden(self, arg0: bool) -> None: ...


class XLSheet:
    def __init__(self, *args, **kwargs) -> None: ...

    def chartsheet(self) -> XLChartsheet: ...

    def clone(self, arg0: str) -> None: ...

    def color(self) -> XLColor: ...

    def index(self, arg0: int) -> None: ...

    def isChartsheet(self) -> bool: ...

    def isWorksheet(self) -> bool: ...

    def name(self) -> str: ...

    def setColor(self, arg0: XLColor) -> None: ...

    def setIndex(self, arg0: int) -> None: ...

    def setName(self, arg0: str) -> None: ...

    def setSelected(self, arg0: bool) -> None: ...

    def setVisibility(self, arg0) -> None: ...

    def visibility(self, *args, **kwargs) -> Any: ...

    def worksheet(self, *args, **kwargs) -> Any: ...


class XLSheetState:
    Hidden: Any = ...
    VeryHidden: Any = ...
    Visible: Any = ...
    __entries: Any = ...

    def __init__(self, arg0: int) -> None: ...

    def __eq__(self, other) -> Any: ...

    def __getstate__(self) -> Any: ...

    def __hash__(self) -> Any: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __ne__(self, other) -> Any: ...

    def __setstate__(self, state) -> Any: ...

    @property
    def name(self) -> Any: ...

    @property
    def __doc__(self) -> Any: ...

    @property
    def __members__(self) -> Any: ...


class XLSheetType:
    Chartsheet: Any = ...
    Dialogsheet: Any = ...
    Macrosheet: Any = ...
    Worksheet: Any = ...
    __entries: Any = ...

    def __init__(self, arg0: int) -> None: ...

    def __eq__(self, other) -> Any: ...

    def __getstate__(self) -> Any: ...

    def __hash__(self) -> Any: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __ne__(self, other) -> Any: ...

    def __setstate__(self, state) -> Any: ...

    @property
    def name(self) -> Any: ...

    @property
    def __doc__(self) -> Any: ...

    @property
    def __members__(self) -> Any: ...


class XLValueType:
    Boolean: Any = ...
    Empty: Any = ...
    Error: Any = ...
    Float: Any = ...
    Integer: Any = ...
    String: Any = ...
    __entries: Any = ...

    def __init__(self, arg0: int) -> None: ...

    def __eq__(self, other) -> Any: ...

    def __getstate__(self) -> Any: ...

    def __hash__(self) -> Any: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __ne__(self, other) -> Any: ...

    def __setstate__(self, state) -> Any: ...

    @property
    def name(self) -> Any: ...

    @property
    def __doc__(self) -> Any: ...

    @property
    def __members__(self) -> Any: ...


class XLWorkbook:
    def __init__(self, *args, **kwargs) -> None: ...

    def addWorksheet(self, arg0: str) -> None: ...

    def chartsheet(self, arg0: str) -> XLChartsheet: ...

    def chartsheetCount(self) -> int: ...

    def chartsheetExists(self, arg0: str) -> bool: ...

    def chartsheetNames(self) -> List[str]: ...

    def cloneSheet(self, arg0: str, arg1: str) -> None: ...

    def deleteNamedRanges(self) -> None: ...

    def deleteSheet(self, arg0: str) -> None: ...

    def setSheetIndex(self, arg0: str, arg1: int) -> None: ...

    @overload
    def sheet(self, arg0: int) -> XLSheet: ...

    @overload
    def sheet(self, arg0: str) -> XLSheet: ...

    @overload
    def sheet(*args, **kwargs) -> Any: ...

    def sheetCount(self) -> int: ...

    def sheetExists(self, arg0: str) -> bool: ...

    def sheetNames(self) -> List[str]: ...

    @overload
    def typeOfSheet(self, arg0: int) -> XLSheetType: ...

    @overload
    def typeOfSheet(self, arg0: str) -> XLSheetType: ...

    @overload
    def typeOfSheet(*args, **kwargs) -> Any: ...

    def worksheet(self, *args, **kwargs) -> Any: ...

    def worksheetCount(self) -> int: ...

    def worksheetExists(self, arg0: str) -> bool: ...

    def worksheetNames(self) -> List[str]: ...


class XLWorksheet:
    def __init__(self, *args, **kwargs) -> None: ...

    @overload
    def cell(self, arg0: str) -> XLCell: ...

    @overload
    def cell(self, arg0: XLCellReference) -> XLCell: ...

    @overload
    def cell(self, arg0: int, arg1: int) -> XLCell: ...

    @overload
    def cell(*args, **kwargs) -> Any: ...

    def clone(self, arg0: str) -> None: ...

    def color(self) -> XLColor: ...

    def column(self, arg0: int) -> XLColumn: ...

    def columnCount(self) -> int: ...

    def index(self, arg0: int) -> None: ...

    def isSelected(self) -> bool: ...

    def lastCell(self) -> XLCellReference: ...

    def name(self) -> str: ...

    @overload
    def range(self) -> XLCellRange: ...

    @overload
    def range(self, arg0: XLCellReference, arg1: XLCellReference) -> XLCellRange: ...

    @overload
    def range(*args, **kwargs) -> Any: ...

    def row(self, arg0: int) -> XLRow: ...

    def rowCount(self) -> int: ...

    def setColor(self, arg0: XLColor) -> None: ...

    def setIndex(self, arg0: int) -> None: ...

    def setName(self, arg0: str) -> None: ...

    def setSelected(self, arg0: bool) -> None: ...

    def setVisibility(self, arg0: XLSheetState) -> None: ...

    def visibility(self) -> XLSheetState: ...