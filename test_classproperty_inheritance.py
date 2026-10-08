import pytest

from jaraco.classes.properties import classproperty


class Base(metaclass=classproperty.Meta):
    value = 0

    @classproperty
    def setting(cls):
        return cls.value

    @setting.setter
    def setting(cls, value):
        cls.value = value


def test_inherited_setter_preserves_the_property():
    class Child(Base):
        pass

    Child.setting = 3
    assert Child.value == 3
    assert Child().setting == 3
    assert Base.value == 0
    Child.value = 4
    assert Child.setting == 4
    Child().setting = 5
    assert Child.setting == 5


def test_inherited_read_only_property_cannot_be_overwritten():
    class Parent(metaclass=classproperty.Meta):
        @classproperty
        def setting(cls):
            return 1

    class Child(Parent):
        pass

    with pytest.raises(AttributeError, match="can't set attribute"):
        Child.setting = 2
    assert Child.setting == 1


def test_metaclass_subclass_passes_the_owner_to_the_setter():
    class Meta(classproperty.Meta):
        pass

    class Child(Base, metaclass=Meta):
        @classproperty
        def setting(cls):
            return cls.value

        @setting.setter
        def setting(cls, value):
            cls.value = value

    Child.setting = 3
    assert Child.value == 3
    assert 'value' not in vars(Meta)
    Child().setting = 4
    assert Child.setting == 4


def test_property_subclass_uses_its_setter():
    class Property(classproperty):
        pass

    class Child(Base):
        @Property
        def setting(cls):
            return cls.value

        @setting.setter
        def setting(cls, value):
            cls.value = value

    Child.setting = 3
    assert Child.value == 3
    Child.value = 4
    assert Child.setting == 4
