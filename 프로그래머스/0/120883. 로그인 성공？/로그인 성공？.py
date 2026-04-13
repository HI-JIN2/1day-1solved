def solution(id_pw, db):
    
    result = dict(db).get(id_pw[0])
    
    if result :
        if result == id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"    
