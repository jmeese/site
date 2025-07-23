module Jekyll
  module ArchivesV2
    class Archives
      def generate(site)
        # override to disable archive generation
        Jekyll.logger.warn "jekyll-archives-v2", "Archives generation skipped by override"
      end
    end
  end
end