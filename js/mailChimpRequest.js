// requesst js

function request_mailchimp() {
    
    var data = {
        "email_address": "majix10165@wpfoo.com",
        "status": "subscribed",
        "merge_fields": {
          "FNAME": "",
          "LNAME": ""
        }
    }

              var newsLetterEndPoint = '';

              // fazer o POST com o ajax
              $.ajax({
                type: "POST",
                url: newsLetterEndPoint,
                data: data,
                // se der certo
                success: function() {

                },
                // se der errado
                error: function() {

                },

                // tipo de dados a enviar
                dataType: 'json'
              })
          }
