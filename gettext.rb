require 'nokogiri'

Dir.glob('html/*').each do |hfile|
  html = Nokogiri::HTML(open hfile)

  filename = File.basename(hfile,'.html')
  text = html.at('.document-body-text').inner_text

  begin
   file = File.open("text/#{filename}.txt", 'w')
   file.write text
  rescue IOError => e
    puts "Could not open file for writing."
  ensure
    file.close unless file.nil?
  end
end
