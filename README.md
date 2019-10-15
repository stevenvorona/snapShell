# snapShell
case art generator for snapcodes in python


Backend process ordering:
1) On base page, have user select two colors and a Username
  a) Image process --> Seller
    i) Route hex and username to main script which generates 1:2 PNG for case Image
    ii) Use either PhantomJS or SMTP to create invoice for case maker
  b) Payment
    i) Cretae PayPal or Venmo invoice
   ii) On-payment event JS listener triggers payment from main buyer (mine) account
