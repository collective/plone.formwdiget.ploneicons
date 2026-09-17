import { BasePattern } from "@patternslib/patternslib/src/core/basepattern";
import Parser from "@patternslib/patternslib/src/core/parser";
import registry from "@patternslib/patternslib/src/core/registry";

export const parser = new Parser("plone-icon-selector");

class Pattern extends BasePattern {
    static name = "plone-icon-selector";
    static trigger = ".pat-plone-icon-selector";
    static parser = parser;

    async init() {
        this.input = this.el.querySelector("input");
        this.preview = this.el.querySelector(".icon-preview i");
        
        // The modal is now inside the widget template
        const widgetId = this.input.id;
        this.modal = document.getElementById(`icon-modal-${widgetId}`);
        
        if (this.modal) {
            this.initModalEvents(this.modal);
        }
    }

    initModalEvents(modal) {
        const search = modal.querySelector(".pat-plone-icon-search");
        const icons = modal.querySelectorAll(".icon-select-button");

        if (search) {
            search.addEventListener("input", (e) => {
                const term = e.target.value.toLowerCase();
                icons.forEach((btn) => {
                    const name = btn.dataset.icon.toLowerCase();
                    const col = btn.closest(".col");
                    if (col) {
                        col.style.display = name.includes(term) ? "" : "none";
                    }
                });
            });
        }

        icons.forEach((btn) => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                const icon = btn.dataset.icon;
                this.updateValue(icon);
                // Plone's data-bs-dismiss="modal" handles the closing
            });
        });
    }

    updateValue(icon) {
        if (this.input) {
            this.input.value = icon;
            this.input.dispatchEvent(new Event("change", { bubbles: true }));
        }
        if (this.preview) {
            this.preview.className = `bi bi-${icon}`;
        }
    }
}

registry.register(Pattern);
export default Pattern;
export { Pattern };
