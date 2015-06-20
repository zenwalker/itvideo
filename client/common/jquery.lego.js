(function($) {

  $.fn.ctx = function(ctx) {
    this.selector = '.' + ctx;
    return this;
  };

  $.fn.elem = function(elemName) {
    return $(this.selector + '_' + elemName, this);
  };

  $.fn.setMod = function(mod) {
    return this.addClass('-' + mod);
  };

  $.fn.delMod = function(mod) {
    return this.removeClass('-' + mod);
  };

  $.fn.hasMod = function() {
    return this.hasClass('-' + mod);
  };

}(jQuery));
