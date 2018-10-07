class HomeController < ApplicationController
  def top
  @text = File.read("/Users/aochaaaaannnn/lesson/python/Scraping_demo/db/nikkei_heikin.csv").chomp
  p "---------"
  p @text
  p "---------"
  end
end
