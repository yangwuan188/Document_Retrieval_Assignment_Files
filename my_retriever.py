import math
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.newindex={}
        self.df={}
        self.idf={}
        # create a newindex dictionary
        for term in index:
            #store df of each term into a dict
            self.df.update({term:len(index[term])})
            for docid,value in index[term].items():
                if docid not in self.newindex.keys():
                    self.newindex[docid]={}
                self.newindex[docid][term]=value               
        D=len(self.newindex)
        for key in self.df:
            #calculate idf value
            self.idf[key]=math.log(D/self.df[key],10)

    # Method performing retrieval for specified query
    def forQuery(self, query):
        #judge termweighting
        if self.termWeighting =='tf':
            cos={}
            for docid in self.newindex:
                di=0
                fenzi=0
                for term in self.newindex[docid]:
                    #cumulate the value of d
                    di+=self.newindex[docid][term]**2        
                    if term in query.keys():
                        #cumulate the value of molecule 
                        fenzi+=(query[term])*(self.newindex[docid][term])
                #calculate cosine 
                cosine=fenzi/math.sqrt(di)
                #store eache consine into dict
                cos.update({docid:cosine})
            #sort the value of cosine   
            sortcos=sorted(cos.items(),key = lambda cos:cos[1],reverse=True)
            list=[]
            #store the docid of cosine value into a list
            for i in range(0,len(sortcos)):
                list.append(int(sortcos[i][0]))       
            return list
          #judge termweighting
        if self.termWeighting == 'tfidf':
            cos={}
            for docid in self.newindex:
                di=0
                fenzi=0
                for term in self.newindex[docid]:
                    di+=(self.newindex[docid][term]*self.idf[term])**2
                    if term in query.keys():
                        #cumulate the value of molecule
                        fenzi+=(query[term]*self.idf[term])*(self.newindex[docid][term]*self.idf[term])
                cosine=fenzi/math.sqrt(di)
                cos.update({docid:cosine})
            sortcos=sorted(cos.items(),key = lambda cos:cos[1],reverse=True)
            list=[]
            #store the docid of cosine value into a list
            for i in range(0,len(sortcos)):
                list.append(int(sortcos[i][0]))       
            return list
          #judge termweighting
        if self.termWeighting == 'binary':
            cos={}
            for docid in self.newindex:
                fenzi=0
                di=len(self.newindex[docid])
                for term in self.newindex[docid]:
                    if term in query.keys():
                        #cumulate the value of molecule
                        fenzi+=1  
                cosine=fenzi/math.sqrt(di)
                cos.update({docid:cosine})
            sortcos=sorted(cos.items(),key = lambda cos:cos[1],reverse=True)
            list=[]
            #store the docid of cosine value into a list
            for i in range(0,len(sortcos)):
                list.append(int(sortcos[i][0]))       
            return list
            
                        
                    
                    
            
            
        
                
            
            
            
        

