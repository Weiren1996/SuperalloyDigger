# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:06:30 2020

@author: 35732
"""
import xlrd
import xlwt
import os
from pre_processor import Pre_processor
from sentence_positioner import Sentence_Positioner
from T_pre_processor import T_pre_processor

class All_attributes:
    def __init__(self,prop_name,txt_name,text_path,triple_path,out_path,C_path):
        self.txt_name = txt_name
        self.text_path = text_path
        self.triple_path = triple_path
        self.prop_name = prop_name
        self.out_path = out_path
        self.C_path = C_path
    def get_toexcel(self):
        xls = xlwt.Workbook()
        sheet = xls.add_sheet("all_attributes")
        sheet.write(0,0,'txt_name')
        sheet.write(0,1,'Full_text')
        sheet.write(0,2,'Target_sentences')
        sheet.write(0,3,'alloy')
        sheet.write(0,4,'property')
        sheet.write(0,5,'value')
        
        
        #triples_tuple
        data_triples = xlrd.open_workbook(self.triple_path)
        table_triples = data_triples.sheet_by_index(0)
        for x in range(0,len(table_triples.col_values(0))):
            sheet.write(x+1,1,str(table_triples.col_values(0)[x]))
            sheet.write(x+1,2,str(table_triples.col_values(1)[x]))  
            sheet.write(x+1,3,str(table_triples.col_values(2)[x]))  
            sheet.write(x+1,4,str(table_triples.col_values(3)[x]))  
            sheet.write(x+1,5,str(table_triples.col_values(4)[x]))  
        
        #txt_name
        k = 0
        for i in range(0,len(table_triples.col_values(0))):
            if table_triples.col_values(0)[i]:
                sheet.write(i+1,0,str(self.txt_name[k]))
                k += 1
        #text + filtered_text_1 + Target sentences
        txt_name = os.listdir(self.text_path) 
        process_text = []
        for i in range(0,len(txt_name)):
            file = open(self.text_path + '/'+str(i)+'.txt' ,'r',encoding='utf-8')#+str(i)+'.txt'
            sole_text = file.read()

#            sheet.write(i+1,1,path)
            pre_processor = Pre_processor(sole_text,self.C_path)
            filter_txt = pre_processor.pre_processor()#第二次对语料进行处理
            path_2 = self.text_path +'/proprecess'
            isExists =os.path.exists(path_2)
            if isExists:
                text_path = path_2 + '/'+str(i)+'.txt' 
                file = open(text_path ,'w',encoding='utf-8')
                file.write(filter_txt)
                process_text.append(text_path)

            else:
                os.makedirs(path_2)
                text_path = path_2 + '/'+str(i)+'.txt' 
                file = open(text_path ,'w',encoding='utf-8')
                file.write(filter_txt)
                process_text.append(text_path)

        xls.save(self.out_path)
            
            
        
        