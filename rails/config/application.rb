require_relative "boot"
require "rails"

module RailsApp
  class Application < Rails::Application
    config.load_defaults 7.0
  end
end
