{{ objname | escape | underline }}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
   :special-members:
      
   .. raw:: html

      <hr>

   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods summary') }}

   .. autosummary::
      :nosignatures:
   {% for item in all_methods %}
      {% if not item.startswith('_') or item in included_special_methods %}
         ~{{ name }}.{{ item }}
      {% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes summary') }}

   .. autosummary::
   {% for item in attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   .. raw:: html

      <hr>

