//
// Created by Kenneth Balslev on 02/06/2017.
//

#include "XLColumn.h"
#include "XLWorksheet.h"

using namespace std;
using namespace RapidXLSX;

/**
 * @details Assumes each node only has data for one column.
 */
XLColumn::XLColumn(XLWorksheet &parent,
                   XMLNode &columnNode)
    : m_parentWorksheet(&parent),
      m_parentDocument(&parent.ParentDocument()),
      m_columnNode(&columnNode),
      m_width(10),
      m_hidden(false),
      m_column(0)
{
    // Read the 'min' attribute of the Column
    auto minmaxAtt = m_columnNode->attribute("min");
    if (minmaxAtt != nullptr) m_column = stoul(minmaxAtt->value());

    // Read the 'Width' attribute of the Column
    auto widthAtt = m_columnNode->attribute("width");
    if (widthAtt != nullptr) m_width = stof(widthAtt->value());

    // Read the 'hidden' attribute of the Column.
    auto hiddenAtt = m_columnNode->attribute("hidden");
    if (hiddenAtt != nullptr) {
        if (hiddenAtt->value() == "1") m_hidden = true;
        else m_hidden = false;
    }
}

/**
 * @details
 */
float XLColumn::Width() const
{
    return m_width;
}

/**
 * @details
 */
void XLColumn::SetWidth(float width)
{
    m_width = width;

    // Set the 'Width' attribute for the Cell. If it does not exist, create it.
    auto widthAtt = m_columnNode->attribute("width");
    if (widthAtt == nullptr) {
        widthAtt = m_parentWorksheet->XmlDocument().createAttribute("width", to_string(m_width));
        m_columnNode->appendAttribute(widthAtt);
    }
    else {
        widthAtt->setValue(m_width);
    }

    // Set the 'customWidth' attribute for the Cell. If it does not exist, create it.
    auto customAtt = m_columnNode->attribute("customWidth");
    if (customAtt == nullptr) {
        customAtt = m_parentWorksheet->XmlDocument().createAttribute("customWidth", "1");
        m_columnNode->appendAttribute(customAtt);
    }
    else {
        customAtt->setValue("1");
    }
}

/**
 * @details
 */
bool XLColumn::Ishidden() const
{
    return m_hidden;
}

/**
 * @details
 */
void XLColumn::SetHidden(bool state)
{
    m_hidden = state;

    std::string hiddenstate;
    if (m_hidden) hiddenstate = "1";
    else hiddenstate = "0";

    // Set the 'hidden' attribute for the Cell. If it does not exist, create it.
    auto hiddenAtt = m_columnNode->attribute("hidden");
    if (hiddenAtt == nullptr) {
        hiddenAtt = m_parentWorksheet->XmlDocument().createAttribute("hidden", hiddenstate);
        m_columnNode->appendAttribute(hiddenAtt);
    }
    else {
        hiddenAtt->setValue(hiddenstate);
    }
}

/**
 * @details
 */
XMLNode &XLColumn::ColumnNode()
{
    return *m_columnNode;
}