def get_prompt():
    return '''Please retrieve Name,email_id,mob_number,qualification,experience,skills,certification,achievement from 
    the following resume article. If you can't find the information from this article then return "". if there is no 
    experience return "Fresher",if there is not skills,certification,achievements return "NIL". Do not make things 
    up. Always return your response as a valid JSON string. The format of that string should be this,

    {
              "Name":"Name",
              "email_id":"email@gmail.com,
              "mob_number":"8138032213",
              "qualification":"Bachelor of computer Application",
              "experience" : "Fresher", 
              "skills" : "python,datascience,machinelearning,nlp",
              "certification" :"IBM Data Analyst with python,
              "achievement": "NIL"
           }
           News Article:
           ============


           '''