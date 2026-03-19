#include<iostream>
#include<queue>
using namespace std;

int main(){
    int testCase,N, M,star,count;


    cin>>testCase;
    for(int i=0;i<testCase;i++){
        count=0;
        cin>>N>>M;
        queue<pair<int,int>>q;
        priority_queue<int>pq; //우선순위 큐

        for(int j=0;j<N;j++){
            cin>>star; 
            q.push({j,star}); //인덱스, 중요도
            pq.push(star); //중요도
        }

        while(!q.empty()){
            int curIndex=q.front().first;
            int curValue=q.front().second;
            q.pop();
            if(pq.top()==curValue){ //우선순위 큐의 top이랑 현재 중요도가 같으면 출력하고 카운트 업
                pq.pop();
                count++;
                if(curIndex==M){ //원하던 프린트가 출력되면 현재 카운트 출력
                    cout<<count<<endl;
                    break;
                }
            }
            else q.push({curIndex,curValue});//중요도 낮으면 다시 넣기
        }
    }
}