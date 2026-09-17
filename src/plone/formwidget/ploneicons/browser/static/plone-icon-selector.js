import BasePattern from "@patternslib/patternslib/src/core/base";
import Parser from "@patternslib/patternslib/src/core/parser";

const parser = new Parser("plone-icon-selector");
parser.addArgument("baseUrl", "");

export default BasePattern.extend({
  name: "plone-icon-selector",
  trigger: ".pat-plone-icon-selector",

  init() {
    this.options = parser.parse(this.el, this.options);
    this.$input = this.$("input");
    this.$preview = this.$(".icon-preview i");
    this.$button = this.$(".icon-selector-button");

    this.$button.on("click", (e) => {
      e.preventDefault();
      this.openModal();
    });
  },

  openModal() {
    const modalUrl = `${this.options.baseUrl}/@@icon-selector-modal`;
    
    // We use Plone's native pat-modal via a dynamic trigger
    const $link = $(`<a href="${modalUrl}" class="pat-modal" data-pat-modal="title: Select Icon; width: 600px"></a>`);
    $link.appendTo("body").on("patterns-injected", (e) => {
      this.initModalEvents($(e.target));
    }).click();
    $link.remove();
  },

  initModalEvents($modal) {
    const $search = $modal.find(".pat-plone-icon-search");
    const $icons = $modal.find(".icon-select-button");

    $search.on("input", (e) => {
      const term = e.target.value.toLowerCase();
      $icons.each((i, el) => {
        const $el = $(el);
        const name = $el.data("icon").toLowerCase();
        $el.closest(".col").toggle(name.includes(term));
      });
    });

    $icons.on("click", (e) => {
      e.preventDefault();
      const icon = $(e.currentTarget).data("icon");
      this.updateValue(icon);
      // Close the modal
      $modal.closest(".plone-modal-wrapper").find(".plone-modal-close").click();
    });
  },

  updateValue(icon) {
    // Check if we need full class name
    let value = icon;
    if (this.el.classList.contains("plone-icons-full-classname-widget-wrapper") || 
        this.$input.hasClass("plone-icons-full-classname-widget")) {
        value = `bi-${icon}`;
    }
    
    this.$input.val(value);
    this.$preview.attr("class", `bi bi-${icon}`);
    this.$input.trigger("change");
  }
});
