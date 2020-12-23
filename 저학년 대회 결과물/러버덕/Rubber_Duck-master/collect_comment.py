import steamreviews

request_params = dict()
request_params['language'] = 'korean'

# app_ids = [730, 1091500, 570, 578080, 271590]
app_ids = [271590]
steamreviews.download_reviews_for_app_id_batch(app_ids, chosen_request_params=request_params)
