wb=openpyxl.load_workbook(r'####')
ws=wb['Sheet1']
    
#borderline
#def set_border(WS):
    #thin = Side(border_style="thin", color="000000")
thin_border = Border(bottom=Side(style='thin'))
for row in ws:
        
    for cell in row:
        if len(str(cell.value)) > 0:
            cell.border = thin_border            

#set_border(ws)        
#Creating spacing for cell with respect to length            
for col in ws.columns:
    max_length = 0
    column = get_column_letter(col[0].column)  # Get the column name
    # Since Openpyxl 2.6, the column name is  ".column_letter" as .column became the column number (1-based)
    for cell in col:
        try:  # Necessary to avoid error on empty cells
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2
    ws.column_dimensions[column].width = adjusted_width
wb.save(r'######')
