require 'nokogiri'
require 'open-uri'

Dir.glob('html/*').each do |file|

  # html = Nokogiri::HTML(open 'docs/1.html')
  #
  # text  = html.at('.document-body-text').inner_text
  # puts text

  html = Nokogiri::HTML(open file)

  text = html.at('.document-body-text').inner_text
  puts text
end
