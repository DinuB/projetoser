import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
  "api_key": "94a3ac9b6dacd4f3d1bb49a910624e06-us2",
  "server": "us2"
})

list_id = "2cdd0ea307"

member_info = {
    "email_address": "majix10165@wpfoo.com",
    "status": "subscribed",
    "merge_fields": {
      "FNAME": "",
      "LNAME": ""
    }
  }

try:
  response = mailchimp.lists.add_list_member(list_id, member_info)
  print("response: {}".format(response))
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))